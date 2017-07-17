package application;

import java.util.HashSet;
import java.util.Set;

import javax.ws.rs.core.Application;

public class RestApplication extends Application {
//add all the Webservice classes to Application class
//this application class is mapped in Web.xml
	
	@Override
    public Set<Class<?>> getClasses() {
        Set<Class<?>> classes = new HashSet<Class<?>>();
        classes.add(service.PatientRestFulWebservice.class);
        //if you have another webservice add here
        return classes;
    }

}
