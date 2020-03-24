package com.test.utils;


import java.io.IOException;
import java.nio.charset.Charset;
import java.util.ArrayList;

import org.testng.annotations.Test;

import com.csvreader.CsvReader;

public class CsvProcess {
	
	
	public static Object[][] readCsv(String path){
		try {
		ArrayList<String[]> csvFile = new ArrayList<String[]>();
		CsvReader reader = new CsvReader(path,',',Charset.forName("utf-8"));
		reader.readHeaders();
		while(reader.readRecord()) {
			System.out.println(reader.getRawRecord());
			csvFile.add(reader.getValues());
		}
		reader.close();
		
		Object[][] result = new Object[csvFile.size()][csvFile.get(0).length];
		for(int row = 0;row<csvFile.size();row++) {
			result[row] = csvFile.get(row);
		}
		
		return result;
		}catch(IOException e) {
			e.printStackTrace();
		}
		return null;
	} 
	
	public static void main(String[] args) {
		readCsv("/Users/weiyi/eclipse-workspace/test2/com.auto/src/test/resources/Case.csv");
	}
}
