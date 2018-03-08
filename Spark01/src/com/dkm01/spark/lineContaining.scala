package com.dkm01.spark

import org.apache.spark.SparkConf
import org.apache.spark.SparkContext

object lineContaining {
  
  def main(args: Array[String]){
    val conf = new SparkConf().setAppName("lineContaining").setMaster("local")
    val sc = new SparkContext(conf)
    
    //val tf = sc.textFile("testData.txt")
    val tf = sc.textFile("file:/E:/Spark/ScalaSparkWS01/Spark01/testData.txt")
    val lc = tf.filter(x => x.contains("Hadoop"))
    lc.count()
    lc.collect()
    lc.first()
    lc.collect().foreach(println)
  }
}