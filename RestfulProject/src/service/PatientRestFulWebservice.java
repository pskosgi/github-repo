package service;

import javax.ws.rs.Consumes;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import bean.PatientData;
import dao.PatientDAO;


@Path("/pateint/")
public class PatientRestFulWebservice {
	
	@POST
	@Consumes({MediaType.APPLICATION_JSON,MediaType.APPLICATION_XML})
	@Produces({ MediaType.APPLICATION_JSON, MediaType.APPLICATION_XML })
	@Path("/name/")
	public PatientData pateintDataByName(String patientName){
		PatientDAO dao = new PatientDAO();
		PatientData pd = dao.getPatentDataByName(patientName);
		
		return pd;
	}
	
	@POST
	@Consumes({MediaType.APPLICATION_JSON,MediaType.APPLICATION_XML})
	@Produces({ MediaType.APPLICATION_JSON, MediaType.APPLICATION_XML })
	@Path("/id/")
	public void pateintDataByID(){
	//	TODO: 
	}
	
	

}
