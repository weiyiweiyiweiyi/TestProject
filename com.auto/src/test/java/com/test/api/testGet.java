package com.test.api;

import java.io.IOException;

import org.apache.http.client.ClientProtocolException;
import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import com.alibaba.fastjson.JSONObject;
import com.test.client.ResClient;
import com.test.utils.CsvProcess;
import com.test.utils.JsonParser;

public class testGet extends TestAPI{
	String urlTest;
	ResClient clientTest;
	int responseCodeTest;
	JSONObject reponseJsonTest;
	JsonParser jsonparserTest;
	Object[][] csvData;
	
	@BeforeClass
	public void beforeClass() throws ClientProtocolException, IOException {
		//读取csv用例文件
		csvData = CsvProcess.readCsv(testDatePath);
	}
	
	@Test
	public void TestRequest() throws ClientProtocolException, IOException {
		//从二维数组里面读取数据：path，checkPoint，expectResult
		for(int i=0;i<csvData.length;i++) {
			String pathTest = csvData[i][2].toString();
			urlTest = host+pathTest;
			String checkPointTest = csvData[i][3].toString();
			String expectResultTest = csvData[i][4].toString();
			
			//发请求，得到实际的响应码
			clientTest = new ResClient();
			clientTest.getWithoutParam(urlTest);
			responseCodeTest = clientTest.responseCode();
					
			//得到实际的响应内容的值
			reponseJsonTest= clientTest.ResponseInJson();
			jsonparserTest = new JsonParser();
			boolean resultStatus = jsonparserTest.value(reponseJsonTest);
			boolean result = jsonparserTest.internalValue(reponseJsonTest,checkPointTest, expectResultTest);
			
			//断言响应中的响应码和响应中的值
			Assert.assertEquals(responseCodeTest, 200);
			Assert.assertTrue(resultStatus);
			Assert.assertTrue(result);
			
		}
	}
}
