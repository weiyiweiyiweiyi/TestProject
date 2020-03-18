package com.test.client;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.http.Header;
import org.apache.http.HttpEntity;
import org.apache.http.NameValuePair;
import org.apache.http.ParseException;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.client.methods.HttpUriRequest;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;

public class RestfulClient {
	
	//定义请求，参数、客户端，响应,响应码,响应头等变量
	HttpGet requestGet;
	HttpPost requestPost;
	UrlEncodedFormEntity formParam;
	CloseableHttpClient client;
	CloseableHttpResponse response;
	int responseCode;
	Header[] header;
	HttpEntity entity;
	Map<String,String> mapHeader;
	String stringResponse;
	JSONObject jsonResponse;
	
	
	//发送get不带参数的请求，并且获得反馈
	public void getWithoutParam(String url) throws ClientProtocolException, IOException {
		requestGet = new HttpGet(url);
		client = HttpClients.createDefault();
		response = client.execute(requestGet);
	}
	
	//发送post带参数请求，参数为form表单形式
	public void postWithForms(String url,List<NameValuePair> param) throws ClientProtocolException, IOException {
		requestPost = new HttpPost(url);
		
		//设置form参数和post方法的请求体
		formParam = new UrlEncodedFormEntity(param,"utf-8");
		requestPost.setEntity(formParam);
		
		client = HttpClients.createDefault();
		response = client.execute(requestPost);
	}
	
	
	//获取响应码
	public int responseCode() {
		responseCode = response.getStatusLine().getStatusCode();
		return responseCode;
	}
	
	
	//将响应体转成String格式
	public String ResponseInString() throws ParseException, IOException {
		entity = response.getEntity();
		stringResponse = EntityUtils.toString(entity);
		return stringResponse;
		
	}
	
	
	//将响应体转成json格式
	public JSONObject ResponseInJson() throws ParseException, IOException {
		JSONObject jsonResponse = JSON.parseObject(ResponseInString());
		return jsonResponse;
	}
	
	
	//将Heade[]响应头转为map
	public Map<String,String> ResponseInmap() {
		header = response.getAllHeaders();
		Map<String,String> mapHeader = new HashMap<String,String>();
		for(Header temp:header) {
			mapHeader.put(temp.getName(), temp.getValue());
		}
		return mapHeader;
	}
	
}
