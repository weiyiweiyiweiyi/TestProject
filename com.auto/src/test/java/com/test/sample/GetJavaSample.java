package com.test.sample;

import java.io.IOException;

import org.apache.http.client.ClientProtocolException;
import org.apache.jmeter.config.Arguments;
import org.apache.jmeter.protocol.java.sampler.AbstractJavaSamplerClient;
import org.apache.jmeter.protocol.java.sampler.JavaSamplerContext;
import org.apache.jmeter.samplers.SampleResult;
import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import com.alibaba.fastjson.JSONObject;
import com.test.api.TestAPI;
import com.test.api.testGet;
import com.test.client.ResClient;
import com.test.utils.CsvProcess;
import com.test.utils.JsonParser;

public class GetJavaSample extends AbstractJavaSamplerClient {

	public static void main(String[] args) {
//		Arguments argments = new Arguments();
//		argments.addArgument("app_key", "");

		JavaSamplerContext context = new JavaSamplerContext(null);
		new GetJavaSample().runTest(context);
	}

//	@Override
//	public Arguments getDefaultParameters() {
//		Arguments argments = new Arguments();
//		argments.addArgument("app_key", "");
//		return argments;
//	}

	@Override
	public SampleResult runTest(JavaSamplerContext arg0) {
		// 创建SampleResult类对象，用于记录执行结果并返回
		SampleResult samplerResult = new SampleResult();
		// jmeter 开始统计响应时间标记,定义一个事务，表示这是事务的起始点
		samplerResult.sampleStart();
		// 测试具体的执行代码
		testGet test1 = new testGet();
		try {
			test1.beforeClass();
			test1.TestRequest();
			// 将结果写到jmeter里面
			if (test1.resultFlag) {
				samplerResult.setSuccessful(true);
				samplerResult.setResponseMessage("Pass");
			} else {
				samplerResult.setSuccessful(false);
				samplerResult.setResponseMessage("failed");
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		// jmeter 结束统计响应时间标记,定义一个事务，表示这是事务的结束点
		samplerResult.sampleEnd();
		return samplerResult;

	}

}
