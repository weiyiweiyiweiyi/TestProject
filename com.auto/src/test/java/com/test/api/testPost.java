package com.test.api;

import org.testng.annotations.Test;
import org.testng.AssertJUnit;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.message.BasicNameValuePair;
import org.testng.Assert;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import com.test.client.ResClient;


public class testPost {
	String urlTest="http://127.0.0.1:8899/postp";
	ResClient clientTest;
	List<NameValuePair> param;
	int responseCodeTest;
	String stringResponseTest;
	
	@Test
	public void testAssert() {
		AssertJUnit.assertEquals(responseCodeTest, 200);
		AssertJUnit.assertEquals(stringResponseTest,"带参数post请求");
	}
	
	@BeforeMethod
	public void beforeTest() throws ClientProtocolException, IOException {
		clientTest = new ResClient();
		
		//构造forms形式的参数，用list实现
		List <NameValuePair> param = new ArrayList <NameValuePair>();
		param.add(new BasicNameValuePair("name","hehe"));
		param.add(new BasicNameValuePair("age","20"));
		
		clientTest.postWithForms(urlTest, param);
		responseCodeTest = clientTest.responseCode();
		stringResponseTest = clientTest.ResponseInString();
		//System.out.println(responseCodeTest);
		//System.out.println(stringResponseTest);
	}

}
