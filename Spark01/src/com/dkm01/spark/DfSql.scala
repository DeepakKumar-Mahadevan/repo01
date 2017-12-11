package com.dkm01.spark

import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.sql._

case class bpl_table(team:String, played:Integer, won:Integer, drawn:Integer, lost:Integer, points:Integer);
    
object DfSql {
  def main(args: Array[String]) {

    //Create conf object
    val conf = new SparkConf()
      .setAppName("DFSql").setMaster("local")

    //create spark context object
    val sc = new SparkContext(conf)

    //create spark SqlContext object
    val sqc = new org.apache.spark.sql.SQLContext(sc)
    
    import sqc.implicits._
    
    val bpl_data = sc.textFile("E:\\Chicago_E_Drive\\Deepak DOCs\\Study\\Data Analytics\\Sample_Data\\BPL.csv");
    
    val bpl_data_01 = bpl_data.map(x => x.split(","))
    
    val bpl_data_02 = bpl_data_01.filter(x => x(0) != "TEAM")
    
    //Error: case class should be declared outside the object
    //case class bpl_table(team:String, played:Integer, won:Integer, drawn:Integer, lost:Integer, points:Integer);
    
    val bplt = bpl_data_02.map(x => bpl_table(x(0), x(1).toInt, x(2).toInt, x(3).toInt, x(4).toInt, x(5).toInt));
    
    val bplt_df = bplt.toDF();
    
    bplt_df.show();
    
    bplt_df.printSchema();
    
    bplt_df.select("team","points").show(4);
    
    bplt_df.registerTempTable("BPL_Table");
    
    sqc.sql("Select * from BPL_Table").show(4);
    
    sqc.sql("Select * from BPL_Table order by team asc").show();
    
    sqc.sql("Select * from BPL_Table where lost >= 10").show();
    
    sqc.sql("Select * from BPL_Table where won >= 25").show();

  }
}