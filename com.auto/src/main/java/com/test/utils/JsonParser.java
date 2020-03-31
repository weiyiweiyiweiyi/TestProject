package com.test.utils;

import com.alibaba.fastjson.JSONObject;

/**
 * 将响应信息转为Json格式后，对其进行进一步的解析：传入key得到value的值
 */
public class JsonParser {
	JSONObject internal;
	
	public boolean jsonValue(JSONObject jo,String actualResult,String expectResult) {     //将响应转成的json对象作为参数
	 	JSONObject internal = jo.getJSONObject("result");   //取key为“result”的value值，该值为一个json对象
	 	String checkpoint = internal.getString(actualResult);		//取key为“city”的value的值，并将其转为String类型
		if(checkpoint.equals(expectResult)) {
			return true;
		}else {
			return false;
		}	
	}
}