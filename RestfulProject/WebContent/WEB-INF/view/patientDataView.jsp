<!DOCTYPE html>
<html>
<head>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions"%>

<title>Patient search</title>
<script src="../js/angular.min.js"></script>
<script src="../js/jquery-3.2.1.min.js"></script>
<script src="../js/patient-search.js"></script>
<link href="../css/patient-search-tool.css" rel="stylesheet" type="text/css"></link>

<script type="text/javascript">

var ctxPath = "<%=request.getContextPath()%>";

    var app = angular.module('postserviceApp', []);
    app.controller('postserviceCtrl', function($scope, $http, $window, $element) {
	$scope.name = null;
	$scope.age = null;
	$scope.adress = null;
	$scope.lblMsg = null;
	$scope.postdata = function(firstNameValue) {
		
	    var data = {
	    		patientName:firstNameValue
	    };
	    
	    $http.post(ctxPath + '/PatientRecod/pateint/name', JSON.stringify(data)).then(
			function(response) {
				if (response.data)
					$scope.finderloader=false;
				 	$scope.PatientData=response.data;
		    }
	    );
	},
	
	
	
    
</script>



</head>
<body bgcolor="#e9e9e9";>
<header>
<label align="center"><h2>Patient Search</h2></label>
</header>
	<div ng-app="postserviceApp" ng-controller="postserviceCtrl">
		<div align="center">
		<table id="maintable" class ="mainsearchbox">
		<tr>
		<td>
			<form name="form" ng-app>
			<table   calss="searchbox">
				<tr>
					<td>PATIENT FIRST NAME<label style="color:red;"><b>*</b></label>:</td>
					<td><input type="text" ng-model="firstName"></td>
				</tr>
				
				
				<tr>
					<td></td>
					<td><input type="submit" value="Search by FirstName"
						ng-click="postdata(firstName)" /></td>
				</tr>
			</table>
			<br />
			</form>
			
		</td>	
		
	</tr>		
	</table> 
	<!--END of main table 	  -->
			
			
			
			
		</div>

		
		<div ng-show="finderloader" class=spinner id="finderloader">
			<br/>
			<img src="../images/loader-snake.gif"
				style="width: 25px; height: 25px;">
		</div>
		

		
			<table width="100%" border="1" align="center" id="myTable"
				class="myResultTable" nowrap>
				<tr>
					<th>First Name</th>
					<th>Last Name</th>
					<th>Record number</th>
					<th>Address</th>
					<th>Doc Name</th>
					<th>PhoneNumber</th>
					
				</tr>
				<tr >
					<td>{{PatientData.firstName}}</td>
					<td>{{PatientData.lastName}}</td>
					<td>{{PatientData.recordNumber}}</td>
					<td>{{PatientData.address}}</td>
					<td>{{PatientData.patentPrimaryDoctor}}</td>
					<td>{{PatientData.phoneNumber}}</td>
				</tr>

			</table>
			
	
<footer>
<br/>
</footer>
</body>
</html>