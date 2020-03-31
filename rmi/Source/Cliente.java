/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rmiExample.Cliente;

/**
 *
 * @author CARLOS MARIO
 */

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import rmiExample.Common.IServidor;

public class Cliente {
	private static IServidor servidor = null;
	
	public static void main(String[] args) throws Exception {
		Registry registry = LocateRegistry.getRegistry(9999);
		servidor = (IServidor) registry.lookup("remoteServidor");
		servidor.ListarProductos();
	}

}