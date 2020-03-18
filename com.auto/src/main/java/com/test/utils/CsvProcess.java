package com.test.utils;

import java.io.FileInputStream;

public class CsvProcess {
	public Object[][] processCsv(String path){
		FileInputStream file= new FileInputStream(path);
		byte[] buffer = new byte[file.available()];
		int len;
		file
		while((len = file.read(buffer))!=-1) {
			
		}
		
		
		return null;
	} 
	

}
