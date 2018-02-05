package main

import "fmt"

func generate(ch chan<- int) {
	for i := 2; ; i++ {
		ch <- i // Send 'i' to channel 'ch'.
	}
}

func filter(src <-chan int, dst chan<- int, prime int) {
	for i := range src { // Loop over values received from 'src'.
		if i%prime != 0 {
			dst <- i // Send 'i' to channel 'dst'.
		}
	}
}

func sieve() {
	ch := make(chan int) // Create a new channel.
	go generate(ch)      // Start generate() as a subprocess.
	for {
		prime := <-ch
		fmt.Print(prime, "\n")
		ch1 := make(chan int)
		go filter(ch, ch1, prime)
		ch = ch1
	}
}

func main() {
	sieve()
}

// 在generate中的是ch
// 在filter中 ch 是src，ch1是dst
// 每当找到一个素数的时候就会开启一个filter（从第一个2开始，第二个是3）
// 上一个filter的ch1 是 下一个的ch
// 也就是上一个的 dst 会是下一个的 src
// 上一个dst 中存储的是相对当前方法中的prime 除不开的数，（并且第一个除不开的数必然是素数）
// 上一个dst中的数都交给下一个filter的src 让其去判断是不是
// 当控制台中输出了一个素数后，就会又新建一个filter 这个新开的filter 会将上一个dst中的数据 进行又一次的筛选
// 每次的筛选都是上一次筛选剩下的

// ch ch1 都是无缓冲的，只能保存一个元素
// 从ch中读取数据进行循环，比如prime = 2 的时候，是2的倍数的都会被pass掉，
// 不是的就会放入ch1中，ch1如果没有被读取走，从ch中读取的也会暂停

// 当前算出了多少个素数就会有多少个goroutine
