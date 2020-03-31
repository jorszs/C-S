/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rmiexample.Servidor;

/**
 *
 * @author CARLOS MARIO
 */
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import rmiExample.Common.IServidor;

public class Servidor {
	public static void main(String[] args) throws Exception{
                
		ServidorImpl servidor = new ServidorImpl();
		IServidor remote = (IServidor) UnicastRemoteObject.exportObject(servidor, 8801);
		//System.setProperty("java.rmi.server.hostname","192.168.0.13");
		Registry registry  = LocateRegistry.createRegistry(9999);
		
		registry.rebind("remoteServidor", remote);
		
		System.out.println("Servidor Corriendo...\n");
		System.in.read();
		
		registry.unbind("remoteServidor");
		UnicastRemoteObject.unexportObject(servidor, true);
	}

}
