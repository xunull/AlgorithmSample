/**
 * 插入排序
 * 
 * 思想：每次排序的时候，将一个新值 插入到 一个已经排好序的数组中
 */

function insertSort(arr) {
    let i = 1;
    while (i < arr.length) {
        for (let j = 0; j < i; j++) {
            if (arr[j] >= arr[i]) {
                let temp = arr[i];
                let k = i;
                while (k > j) {
                    arr[k] = arr[k - 1];
                    k -= 1;
                }
                arr[j] = temp;
                break;
            }
        }
        i += 1;
    }
}

function test() {
    const tempArr = [2, 6, 3, 12, 62, 1, 56, 100, 25, 89];
    insertSort(tempArr);
    console.log(tempArr);
}

test();
