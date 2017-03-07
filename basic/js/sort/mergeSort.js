/**
 * 思想：分治法
 * 
 * 当对两个已经排好序的数组进行排序时，只需要先比较他们的第一个元素，取最小的，然后拿走，然后接下来比较第一个
 * 这样直到其中一个数组为空，然后将剩下的数组中的内容都放入到新数组中即可
 * 这样合并操作的复杂度是O(n)
 * 
 * 如何获取两个有序的数组呢？可以现将这两个数组在各自分成两个数组，让这两个数组有序，
 * 依次类推，直到只剩一个原始的时候，直接合并就可以了
 * 
 * 这样通过先递归，然后合并的算法 就是归并排序
 * 
 * 归并排序的效率是比较高的，设数列长为N，将数列分开成小数列一共要logN步，每步都是一个合并有序数列的过程，时间复* 杂度可以记为O(N)，故一共为O(N*logN)
 */

function mergeSort(arr, start, end) {
    if (start < end) {
        const resultArr = [];
        const length = end - start + 1;

        const tempArr1 = mergeSort(arr, start, start + Math.floor(length / 2)-1);
        const tempArr2 = mergeSort(arr, start + Math.floor(length / 2), end);

        let i = 0;
        let j = 0;
        while (i < tempArr1.length && j < tempArr2.length) {
            if (tempArr1[i] < tempArr2[j]) {
                resultArr.push(tempArr1[i]);
                i += 1;
            } else {
                resultArr.push(tempArr2[j]);
                j += 1;
            }
        }
        for (; i < tempArr1.length; i += 1) {
            resultArr.push(tempArr1[i]);
        }
        for (; j < tempArr2.length; j += 1) {
            resultArr.push(tempArr2[j]);
        }
        return resultArr;
    } else {
        return [arr[start]];
    }
}

function test() {
    const tempArr = [2, 6, 3, 12, 62, 1, 56, 100, 25, 89];
    const result = mergeSort(tempArr, 0, tempArr.length - 1);
    console.log(result);
}

test();
