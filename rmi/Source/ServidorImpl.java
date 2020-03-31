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

import java.util.ArrayList;
import java.util.Iterator;
import rmiExample.Common.IServidor;


public class ServidorImpl implements IServidor
{
        @Override
	public void ListarProductos()
	{   
		ArrayList<String> Productos = new ArrayList<>();
		Productos.add("Cebolla");
		Productos.add("Lenteja");
		Productos.add("Harinas");
		Productos.add("Tomates");
		Productos.add("Cepillo");
		Productos.add("Plátano");
		Productos.add("Cominos");
		Productos.add("Cerveza");
		Productos.add("Buñuelo");
		Productos.add("vinagre");
		Productos.add("Quesito");
		Productos.add("Gaseosa");
		
		ArrayList<String> Precios = new ArrayList<>();
		Precios.add("1000");
		Precios.add("1600");
		Precios.add("1200");
		Precios.add("1000");
		Precios.add("3400");
		Precios.add("900");
		Precios.add("1400");
		Precios.add("1700");
		Precios.add("800");
		Precios.add("1800");
		Precios.add("2400");
		Precios.add("1200");
		
		int index = 1;
		Iterator<String> nombreIterator = Productos.iterator();
		Iterator<String> precioIterator = Precios.iterator();
		System.out.print("     Inventario\n\n");
		System.out.print("   Producto   Precio\n\n");
		while(nombreIterator.hasNext()){
			String elemento1 = nombreIterator.next();
			String elemento2 = precioIterator.next();
			index=index+1;
			System.out.print(("   ") + elemento1 + "    " + elemento2 + ("\n"));
		}
	}
}
