/**
 * 希尔排序（shell排序）
 * 
 * 思想：
 * 先将整个序列分成几个子序列
 * 子序列是从原序列中提取，以固定某个步长提取元素,然后对其进行直接插入排序
 * 然后减少增量，子序列中的元素越来越多，当增量为1的时候，等于原序列，算法终止
 * 
 * 稳定性：
 * 由于多次插入排序，我们知道一次插入排序是稳定的，不会改变相同元素的相对顺序，但在不同的插入排序过程中，相同的元* 素可能在各自的插入排序中移动，最后其稳定性就会被打乱，所以shell排序是不稳定的
 * 
 * 时间复杂度
 * 希尔增量的时间复杂度是O(n*n)
 */

function shellSort(arr) {
    for (let gap = Math.floor(arr.length / 2); gap > 0; gap -= 1) {
        for (let base = 0; base < gap; base += 1) {
            for (let i = base; i < arr.length; i += gap) {
                if (arr[i] > arr[i + gap]) {
                    let j = i;
                    while (arr[j + gap] < arr[j]) {
                        const temp = arr[j + gap];
                        arr[j + gap] = arr[j];
                        arr[j] = temp;
                        j -= gap;
                    }
                }
            }
        }
    }
}

function test() {
    const tempArr = [2, 6, 3, 12, 62, 1, 56, 100, 25, 89];
    shellSort(tempArr);
    console.log(tempArr);
}

test();
