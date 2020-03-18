package com.test.utils;

import com.alibaba.fastjson.JSONObject;

/**
 * 将响应信息转为Json格式后，对其进行进一步的解析：传入key得到value的值
 */
public class JsonParser {
	JSONObject internal;
	
	public String jsonValue(JSONObject jo) {     //将响应转成的json对象作为参数
	 	JSONObject internal = jo.getJSONObject("result");   //取key为“result”的value值，该值为一个json对象
	 	String cityvalue = internal.getString("city");		//取key为“city”的value的值，并将其转为String类型
		return cityvalue;
		
	}

}
