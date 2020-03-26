package com.test.utils;


import java.util.ArrayList;
import com.csvreader.CsvReader;
public class CsvProcess {
	
	
	public Object[][] readCsv(String path){
		try {
			ArrayList<String[]> csvList = new ArrayList<String[]>();
			CsvReader csvFile = new CsvReader(path,',');
			csvFile.readHeaders(); 	//忽略表头，如果需要表头可注释掉
			while(csvFile.readRecord()) {   //如果有内容返回true
				csvList.add(csvFile.getValues());   //把该行返回的String[]存人，一行数据作为该list的一个元素
			}
			csvFile.close();
			Object[][] csvArray = new Object[csvList.size()][csvList.get(0).length]; //创建二位数组，一行数据作为该数组的一个元素
			for(int i =0;i<csvList.size();i++) {
				csvArray[i] = csvList.get(i);
			}	
			return csvArray;
		}catch(Exception e){
			e.printStackTrace();
		}
			return null;	
	}
}
