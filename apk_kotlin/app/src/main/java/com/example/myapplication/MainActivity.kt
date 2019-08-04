package com.example.myapplication

import android.os.Bundle
import com.google.android.material.snackbar.Snackbar
import androidx.appcompat.app.AppCompatActivity;
import android.view.Menu
import android.view.MenuItem

import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.content_main.*
import android.content.Context
import android.content.Intent
import android.provider.BaseColumns

class MainActivity : AppCompatActivity() {


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setSupportActionBar(toolbar)

        fab.setOnClickListener { view ->
            Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                .setAction("Action", null).show()
        }

        val route1= Route("Ecopetrol Calle 26", "9:00 a.m.", "Lunes-Viernes")
        val route2= Route("Ecopetrol Calle 126", "9:00 a.m.", "Martes y Jueves")
        val route3= Route("Carulla Calle 85", "6:00 a.m.", "Lunes-Viernes")
        val route4= Route("Carvajal", "9:00 a.m.", "Lunes-Sábado")
        val route5= Route("Calle 182", "5:00 a.m.", "Lunes-Viernes")
        val route6= Route("Colina Campestre", "6:00 a.m.", "Lunes y Martes")
        val listRoutes = listOf(route1, route2, route3, route4, route5, route6)

        val adapter = RouteAdapter(this, listRoutes)

        list.adapter = adapter

        list.setOnItemClickListener { parent, view, position, id ->
            val intent = Intent(this, Info::class.java)
            intent.putExtra("route", listRoutes[position])
            startActivity(intent)
        }

    }


    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        // Inflate the menu; this adds items to the action bar if it is present.
        menuInflater.inflate(R.menu.menu_main, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        return when (item.itemId) {
            R.id.action_settings -> true
            else -> super.onOptionsItemSelected(item)
        }
    }
}
