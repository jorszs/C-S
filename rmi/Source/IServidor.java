/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rmiExample.Common;

/**
 *
 * @author CARLOS MARIO
 */
import java.rmi.*;

public interface IServidor extends Remote{
	//Lista de métodos remotos
	public void ListarProductos() throws RemoteException;
	//public void ListarPrecios() throws RemoteException;
}
