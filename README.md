##Baihui##

Baihui API integration for Python

[百会CRM](http://baike.baidu.com/link?url=bDZMl0cQo4NzgwSQ4_6frMJRWgKGeJD4EnaX7wXUGPGSzbZKI6OpvkfhXPM-Y98p6UboYhQEIYUQryM5V2iDJq)是一套企业客户关系管理整体解决方案，提供了丰富多样的功能及管理工具，围绕客户生命周期，将市场活动、线索、商业机会、销售跟踪和预测等进行有机整合，轻松管理企业的销售和市场，更好地维系客户关系，有效缩短销售周期，帮助企业获得更显著的效益。

百会CRM API可以将CRM中的数据以XML或JSON格式导出，用以开发新应用或与第三方业务应用进行集成。由于API与编程语言无关，所以您可以用任何语言开发应用。

参考 [miohtama/mfabrik.zoho](https://github.com/miohtama/mfabrik.zoho) 做一个百会API的python调用接口。

要使用百会的API需要您有百会的帐号以及API的authtoken， 更多详细内容请访问 [百会CRM API 的token生成说明文档](http://statement.wiki.baihui.com/crm/authtoken-introduced.html)


----------

**API 支持**

- [CRM API](http://statement.wiki.baihui.com/api/%E7%99%BE%E4%BC%9ACRM-API.html) 
	<table style="BORDER-LEFT-WIDTH: thin; BORDER-RIGHT-WIDTH: thin; BORDER-TOP-COLOR: #cccccc; BORDER-BOTTOM-WIDTH: thin; BORDER-COLLAPSE: collapse; BORDER-BOTTOM-COLOR: #cccccc; BORDER-RIGHT-COLOR: #cccccc; BORDER-TOP-WIDTH: thin; BORDER-LEFT-COLOR: #cccccc" height="146" width="600" border="0">
	<tbody>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-TOP: #888 1px solid; BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" bgcolor="#f6f6f6" height="50"><strong>方法名称</strong></td>
			<td style="BORDER-TOP: #888 1px solid; BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px" bgcolor="#f6f6f6"><strong>目的</strong></td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="getMyRecords方法" href="http://statement.wiki.baihui.com/api/getMyRecords方法.html">getMyRecords</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">获取API请求中指定的身份验证令牌的所有者的数据</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="getRecords方法" href="http://statement.wiki.baihui.com/api/getRecords方法.html">getRecords</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">获取API请求中指定的所有用户的数据</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="getRecordById方法" href="http://statement.wiki.baihui.com/api/getRecordById方法.html">getRecordById</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">通过记录ID获取个别记录</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="getCVRecords方法" href="http://statement.wiki.baihui.com/api/getCVRecords方法.html">getCVRecords</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">获取百会CRM的自定义视图数据</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="insertRecords方法" href="http://statement.wiki.baihui.com/api/insertRecords方法.html">insertRecords</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">将记录插入到所需的百会CRM模块</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="updateRecords方法" href="http://statement.wiki.baihui.com/api/updateRecords方法.html">updateRecords</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">更新或修改百会CRM的记录</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="getSearchRecords方法" href="http://statement.wiki.baihui.com/api/getSearchRecords方法.html">getSearchRecords</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">通过对选定列的表达式搜索记录</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="getSearchRecordsByPDC方法" href="http://statement.wiki.baihui.com/api/getSearchRecordsByPDC方法.html">getSearchRecordsByPDC</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">根据预先定义的列搜索值</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="deleteRecords方法" href="http://statement.wiki.baihui.com/api/deleteRecords方法.html">deleteRecords</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">删除所选的记录</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="convertLead方法" href="http://statement.wiki.baihui.com/api/convertLead方法.html">convertLead</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">将线索转换为商机、客户和联系人</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="getRelatedRecords方法" href="http://statement.wiki.baihui.com/api/getRelatedRecords方法.html">getRelatedRecords</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">获得主模块的相关记录</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="getFields方法" href="http://statement.wiki.baihui.com/api/getFields方法.html">getFields</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">获取模块中可用字段的详细信息</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="updateRelatedRecords方法" href="http://statement.wiki.baihui.com/api/updateRelatedRecords方法.html">updateRelatedRecords</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">更新与另一条记录相关的记录</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="getUsers方法" href="http://statement.wiki.baihui.com/api/getUsers方法.html">getUsers</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">获取机构用户列表</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="uploadFile方法" href="http://statement.wiki.baihui.com/api/uploadFile方法.html">uploadFile</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">添加附件到记录</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="downloadFile方法" href="http://statement.wiki.baihui.com/api/downloadFile方法.html">downloadFile</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">下载记录附件</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="deleteFile方法" href="http://statement.wiki.baihui.com/api/deleteFile方法.html">deleteFile</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">删除记录附件</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="uploadPhoto方法" href="http://statement.wiki.baihui.com/api/uploadPhoto方法.html">uploadPhoto</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">
				<p>添加照片到某个联系人或线索</p>
			</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="downloadPhoto方法" href="http://statement.wiki.baihui.com/api/downloadPhoto方法.html">downloadPhoto</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">
				<p>下载某个联系人或线索的照片</p>
			</td>
		</tr>
		<tr style="BORDER-BOTTOM-WIDTH: 0px">
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; BORDER-LEFT: #888 1px solid; PADDING-RIGHT: 15px" height="40"><a title="deletePhoto方法" href="http://statement.wiki.baihui.com/api/deletePhoto方法.html">deletePhoto</a></td>
			<td style="BORDER-RIGHT: #888 1px solid; BORDER-BOTTOM: #888 1px solid; COLOR: #3c3c3c; PADDING-BOTTOM: 3px; TEXT-ALIGN: center; PADDING-TOP: 3px; PADDING-LEFT: 15px; PADDING-RIGHT: 15px">
				<p>删除某个联系人或线索的照片</p>
			</td>
		</tr>
	</tbody>
</table>


----------
