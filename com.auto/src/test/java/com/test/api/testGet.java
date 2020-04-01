package com.test.api;

import java.io.IOException;

import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import com.alibaba.fastjson.JSONObject;
import com.test.client.RestfulClient;
import com.test.utils.CsvProcess;
import com.test.utils.JsonParser;

public class testGet extends TestAPI{
	String urlTest="http://127.0.0.1:8899/getjson";
	RestfulClient clientTest;
	int responseCodeTest;
	JSONObject reponseJsonTest;
	JsonParser jsonparserTest;
	String cityValueTest;
	Object[][] csvData;
	
	@Test
	public void TestRequest() {
		//从二维数组里面读取数据：path，checkPoint，expectResult
		for(int i=0;i<csvData.length;i++) {
			String path = 
		}
		
		//得到实际的响应码
		clientTest = new RestfulClient();
		clientTest.getWithoutParam(urlTest);
		responseCodeTest = clientTest.responseCode();
				
		//得到实际的响应内容的值
		reponseJsonTest= clientTest.ResponseInJson();
		jsonparserTest = new JsonParser();
		cityValueTest = jsonparserTest.jsonValue(reponseJsonTest);
		
		//断言响应中的响应码和响应中的result->city的值
		Assert.assertEquals(responseCodeTest, 200);
		Assert.assertEquals(cityValueTest, "chengdu");
	}
	
	@BeforeClass
	public void beforeClass() throws ClientProtocolException, IOException {
		//读取csv用例文件
		csvData = CsvProcess.readCsv(testDatePath);

	}
	
	
}
