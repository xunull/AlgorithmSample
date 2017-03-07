function quickSort(arr, l, r) {
    let i = l;
    let j = r;
    const base = arr[i];
    while (i < j) {
        while (i < j && arr[j] >= base) {
            j -= 1;
        }
        if (i < j) {
            arr[i] = arr[j];
            i += 1;
        }

        while (i < j && arr[i] < base) {
            i += 1;
        }
        if (i < j) {
            arr[j] = arr[i];
            j -= 1;
        }
    }
    arr[i] = base;
    if (l < i) {
        quickSort(arr, l, i - 1);
    }
    if (i < r) {
        quickSort(arr, i + 1, r);
    }
}

/**
 * 这个方法与上面的方法，基本上是一样的
 * 区别在于对是否满足比较添加的判断位置
 * 上面的方法是在方法末尾处判断
 * 下面的方法是在方法开始出判断
 * 
 * 第一种体现的是对后继的约束
 * 第二种体现的是对自己的约束
 * 
 * 第二种可能是多管闲事，但是可以减少一次去方法的调用了
 * @param {*} arr 
 * @param {*} l 
 * @param {*} r 
 */

function quickSortAnother(arr, l, r) {
    if (l < r) {
        let i = l;
        let j = r;
        const base = arr[i];
        while (i < j) {
            while (i < j && arr[j] >= base) {
                j -= 1;
            }
            if (i < j) {
                arr[i] = arr[j];
                i += 1;
            }

            while (i < j && arr[i] < base) {
                i += 1;
            }
            if (i < j) {
                arr[j] = arr[i];
                j -= 1;
            }
        }
        arr[i] = base;
        quickSort(arr, l, i - 1);
        quickSort(arr, i + 1, r);
    }
}

function test() {
    const tempArr = [2, 6, 3, 12, 62, 1, 56, 100, 25, 89];
    quickSort(tempArr, 0, tempArr.length - 1);
    console.log(tempArr);
}

test();
