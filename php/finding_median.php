<?php

$nums1= array(2);
$nums2= array();
$combine = array_merge($nums1,$nums2);
sort($combine); 
$length = count($combine);

if ($length%2 == 0){
    $bottom = $combine[$length/2 - 1];
    $upper = $combine[($length/2)];
    $median = ($bottom + $upper) /2;
} else{
    $median = $combine[$length/2];
}

echo $median;
?>
