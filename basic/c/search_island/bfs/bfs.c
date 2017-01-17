#include <stdio.h>
struct note {
  int x;
  int y;
};

int main() {
  struct note que[2501];
  int head,tail;
  int a[51][51];
  // 数组中所有项都是零
  int book[51][51]={0};

  int i,j,k,sum,max=0;
  int mx,my,n,m,startx,starty,tx,ty;

  // 方向数组
  int next[4][2]={
      {0,1}, // 右
      {1,0}, // 下
      {0,-1}, // 左
      {-1,0} // 上
    };

    // 读入n行m列 以及其实坐标
    // startx starty 是以1开头的
    scanf("%d %d %d %d",&n,&m,&startx,&starty);

    for(i=1;i<=n;i++) {
      for(j=1;j<=n;j++) {
        scanf("%d",&a[i][j]);
      }
    }

    // 队列初始化
    head=1;
    tail=1;

    que[tail].x=startx;
    que[tail].y=starty;
    tail++;
    book[startx][starty]=1;
    sum=1;

    // 当队列不为空的时候循环
    while(head<tail) {
      for(k=0;k<=3;k++) {
        tx=que[head].x+next[k][0];
        ty=que[head].y+next[k][1];

        if(tx<1 || tx>n || ty<1 || ty>m) {
          // 越界了
          continue;
        }

        // 判断是否是陆地，判断是否已经走过
        if(a[tx][ty]>0 && book[tx][ty]==0) {
          sum++;
          book[tx][ty]=1;
          que[tail].x=tx;
          que[tail].y=ty;
          tail++;
        }
      }
      head++;

    }
    printf("%d\n",sum);
    getchar();getchar();
    return 0;
}
