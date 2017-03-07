/**
 * 任意进制的运算
 */

// 引入了readline 使用完后就必须调用close 方法,否则程序不会终止
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    // 如果不设置output ,当使用readline 的question 方法的时候不会有输出
    output: process.stdout,
});

function tenToAny(number, any) {
    const resultArr = [];
    let remainder;
    let quotient = number;
    if (quotient <= any) {
        return quotient;
    }
    do {
        remainder = quotient % any;
        resultArr.unshift(remainder);
        quotient = Math.floor(quotient / any);
    } while (quotient >= any);
    resultArr.unshift(quotient);
    return +resultArr.join('');
}

function anyToTen(number, base) {
    const numberArr = number.toString().split('');
    const length = numberArr.length;
    // 这个如果不设置成0 result 会是NaN
    let result = 0;

    numberArr.forEach((value, index) => {
        result += (+value) * (base ** (length - index - 1));
    });
    return result;
}

rl.question('请输入十进制数字,将其转化为特殊进制 ', (answer) => {
    const temp = answer.trim();
    const num = temp.split(/\s/)[0];
    const base = temp.split(/\s/)[1];
    // 参数需要是数字
    const result = tenToAny(+num, +base);
    console.log(`result is ${result}`);
    console.log(`转换回十进制为  ${anyToTen(result, base)}`);
    rl.close();
});


