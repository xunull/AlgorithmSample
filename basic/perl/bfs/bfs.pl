#!/usr/bin/perl

@mazeArr=();
@bookArr=();
@startCoord=();
@targetCoord=();

# 走下一步的坐标
@nextStep=((-1,0),(0,1),(1,0),(0,-1));
# 最小步数
$minStep=0;
@que=();
$head=0;
$tail=0;

print("输入迷宫,0表示空,1表示有障碍物,以空行结束\n");
while(true){
  $line = <STDIN>;
  if($line eq "\n") {
    last;
  } else {
    @temp =  split(" ",$line);
    push(@mazeArr,[@temp]);
  }
  print @mazeArr

}
print "输入起始坐标:";
$line = <STDIN>;
@startCoord=split(" ",$line);
# print @startCoord;
print "输入目标坐标:";
$line = <STDIN>;
@targetCoord=split(" ",$line);
# print @targetCoord;


for($i=0;$i<=$#mazeArr;$i+=1) {
  print $#mazeArr;
  print "\n";
  foreach $tempVal ($mazeArr[i]) {
   push(@{$bookArr[$i]},"0");
  }
  print @{$bookArr[$i]}

}

# foreach $tempArr (@mazeArr) {
#   @tempArr2=();
#   foreach $tempVal ($tempArr) {
#     # push(@tempArr2,"0");
#     push(@{$bookArr[]})
#   }
#
#   # push(@bookArr,[@tempArr2]);
# }

print @bookArr;
print @bookArr[1]->[1];

bfs();

sub bfs {

  $flag=false;
  while($head<$tail) {
    for($i=0;i<4;$i+=1){
      @currentCoord=($que[$head][0]+$nextStep[i][0],$que[$head][1]+$nextStep[i][1]);
          # if ($currentCoord[0]<0 or $currentCoord[0]> $#mazeArr or $currentCoord[1]<0 or $currentCoord[1]>scalar($mazeArr[0]) {
          #
          # }
    }
  }

}
