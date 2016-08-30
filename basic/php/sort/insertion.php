<?php
// php的分号不能省略，于java 相同


// $sourceArr= [1,5,2,10,5,2,9,10];
$sourceArr= array(100,1,5,2,10,5,2,9,10,12,1,3,4);

insertion($sourceArr);

function insertion($arr) {
  // 不是引用拷贝
  // $tempArr=$arr;

  $tempArr=[];

  // 先插入一个元素
  array_push($tempArr,$arr[0]);
  // for($i=0;$i<count($arr);i++){
  //
  // }
  foreach($arr as $key =>$temp){
      if($key ==0) {
        // 第一个元素已经被push进去了
        // php的foreach 可以相应continue
        continue;
      }
    for($i=0;$i<count($tempArr);$i++){

      if($temp>=$tempArr[$i]){
        if($i+1<count($tempArr)&&$temp<=$tempArr[$i+1]) {
          array_splice($tempArr,$i+1,0,$temp);
          echo $temp.' +++ '.$tempArr[$i];
          break;
        }

        // 已经比到了最后一个元素
        if($i+1==count($tempArr)) {
          array_push($tempArr,$temp);
          echo $temp.' +++ '.$tempArr[$i];
          break;
        }

      }
      // 有可能前面的元素都比此值大，因此，它就是最小的需要放在最前面
      // 但如果能保证第一个被push进去的值，是其中最小的值时(先找出来一个最小的放进去)就不需要这个步骤了
      // 但是这两种方法那个好，也是不一定的，如果先判断最小值，那么这就是一个必然发生的事情
      // 但下面的这部分代码，不一定会被执行到，也不一定会被执行几次
      //

      if($i+1==count($tempArr)) {
        array_unshift($tempArr,$temp);
        break;
      }
    }

  }
  // php的数组排序方法
  // sort($arr);
  print_r($arr);
  print_R($tempArr);
}
 ?>
