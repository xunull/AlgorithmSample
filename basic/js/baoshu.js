// 500 个小孩围成一圈 报数 数到3的人 退出 求最后剩下的人
// 这个用链表方式处理是不是简单些

function baoshu() {

    attr = new Array(500);
    attr.fill(0);

    var index = 0;
    var remain = 500;
    while (true) {
        for (var i = 0; i < 3; i++) {

            while (attr[index] === undefined) {
                index += 1;
                if (index === 500) {
                    index = 0;
                }
            }
            index++;
            if (index === 500) {
                index = 0;
            }

        }
        if (index === 0) {
            index = 499;
        } else {
            index--;
        }

        delete attr[index];
        remain -= 1;
        console.log('remain is ', remain);
        if (remain === 1) {
            break;
        }
    }
    for (var j = 0; j < 500; j++) {
        if (attr[j] !== undefined) {
            console.log(j + 1);
            break;
        }
    }
    console.log(attr);
}

baoshu();
