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
import com.test.client.ResClient;
import com.test.utils.CsvProcess;
import com.test.utils.JsonParser;

public class GetJavaSample extends AbstractJavaSamplerClient{

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
		//创建SampleResult类对象，用于记录执行结果并返回
		SampleResult samplerResult = new SampleResult();
		//jmeter 开始统计响应时间标记,定义一个事务，表示这是事务的起始点
		samplerResult.sampleStart();
		//测试具体的执行代码
		class testGet extends TestAPI{
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
					
					//jmeter 结束统计响应时间标记,定义一个事务，表示这是事务的结束点
					samplerResult.sampleEnd();
					
					//将结果写到jmeter里面
					if(resultStatus) {
						samplerResult.setSuccessful(true);
						samplerResult.setResponseMessage("Pass");
					}else {
						samplerResult.setSuccessful(false);
						samplerResult.setResponseMessage("failed");
					}
					
				}
			}
		}
		
		return samplerResult;				
	}
}
