package com.test.api;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Locale;
import java.util.Properties;
import java.util.ResourceBundle;

import org.testng.annotations.Test;


public class TestAPI {
	Properties prop;
	String host;
	String testDatePath;
	
	@Test
	public  TestAPI() {
		try {
			//数据流的形式读取配置文件
			Properties prop = new Properties();
			prop.load(new FileInputStream ("./src/main/resources/config.properties"));
		}
		catch (Exception e){
			e.printStackTrace();
		}
		
		host = prop.getProperty("host");
		testDatePath = prop.getProperty("testData");
	}
}
