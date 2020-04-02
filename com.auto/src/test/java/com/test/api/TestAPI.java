package com.test.api;

import java.io.FileInputStream;
import java.util.Properties;


public class TestAPI {
	Properties prop;
	String host;
	String testDatePath;
	
	public TestAPI() {
		try {
			//数据流的形式读取配置文件
			Properties prop = new Properties();
			prop.load(new FileInputStream ("./src/main/resources/config.properties"));
			host = prop.getProperty("host");
			testDatePath = prop.getProperty("testData");
		}catch (Exception e){
			e.printStackTrace();
		}
	}
}
