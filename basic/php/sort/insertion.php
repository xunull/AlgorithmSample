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
        if($i+1==count($tempArr)) {
          array_push($tempArr,$temp);
          echo $temp.' +++ '.$tempArr[$i];
          break;
        }
        if($i==count($tempArr)) {
          array_unshift($tempArr,$temp);
        }
      }
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
