package com.test.sample;

import org.apache.jmeter.config.Arguments;
import org.apache.jmeter.protocol.java.sampler.AbstractJavaSamplerClient;
import org.apache.jmeter.protocol.java.sampler.JavaSamplerContext;
import org.apache.jmeter.samplers.SampleResult;
import com.test.api.testGet;
import java.io.IOException;
public class GetJavaSample extends AbstractJavaSamplerClient {

	public static void main(String[] args) {
		Arguments argments = new Arguments();
		argments.addArgument("app_key", "");

		JavaSamplerContext context = new JavaSamplerContext(argments);
		new GetJavaSample().runTest(context);
	}

	@Override
	public Arguments getDefaultParameters() {
		Arguments argments = new Arguments();
		argments.addArgument("app_key", "");
		return argments;
	}

	@Override
	public SampleResult runTest(JavaSamplerContext arg0) {
		System.out.println(System.getProperty("user.dir"));
		// 创建SampleResult类对象，用于记录执行结果并返回
		SampleResult samplerResult = new SampleResult();
		
		// jmeter 开始统计响应时间标记,定义一个事务，表示这是事务的起始点
		samplerResult.sampleStart();
		samplerResult.setSampleLabel("testget");
		
		// 测试具体的执行代码
		testGet test = new testGet();
		try {
			test.beforeClass();
			test.TestRequest();
			// 将结果写到jmeter里面
			if (test.resultFlag) {
				samplerResult.setSuccessful(true);
				samplerResult.setResponseCode("200");
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
