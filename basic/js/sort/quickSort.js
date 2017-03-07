/**
 * 快速排序算法
 * 时间复杂度 N*logN
 * 思想   分治法
 * 
 * 基本思想:
 * 先从数组取一个数作为基准
 * 分组时，将比基准大的数放到一边，比它小的树放到一边
 * 对分组后的区间 重复选择基准，重复分区
 * 
 * 挖坑填数解读:
 * 1. i=L;j=R;  将基准数挖出形成第一个坑arr[i]
 * 2. j-- 由后向前寻找比基准小的数，找到后挖出形成一个坑，并将其放入arr[i]
 * 3. i++ 由前向后寻找比基准大的数，找到后挖出形成一个坑，并将其放入arr[j]
 * 4. 重复上面两步，直到 i==j，将基准数放入arr[i]
 * 
 */

function digPit(arr, i, j) {
    const base = arr[i];
    while (i < j) {
        while (i < j && arr[j] >= base) {
            j -= 1;
        }
        if (i < j) {
            arr[i] = arr[j];
            i += 1;
        }

        while ( i < j && arr[i] < base) {
            i += 1;
        }
        if (i < j) {
            arr[j] = arr[i];
            j -= 1;
        }
    }
    arr[i] = base;

    return i;
}

function quickSort(arr, l, r) {
    if (l < r) {
        const i = digPit(arr, l, r);
        quickSort(arr, l, i - 1);
        quickSort(arr, i + 1, r);
    }
}

function test() {
    const tempArr = [2,6,3,12,62,1,56,100,25,89];
    quickSort(tempArr, 0, tempArr.length - 1);
    console.log(tempArr);
}

test();
