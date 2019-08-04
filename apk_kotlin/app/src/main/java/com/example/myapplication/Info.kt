package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_info.*

class Info : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_info)

        val route = intent.getSerializableExtra("route") as Route

        textView4.text = route.destino
        textView5.text = route.hora
        textView6.text = route.dias
    }
}
