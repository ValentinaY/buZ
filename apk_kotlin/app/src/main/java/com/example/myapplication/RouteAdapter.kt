package com.example.myapplication

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import kotlinx.android.synthetic.main.route.view.*

class RouteAdapter(private val mContext: Context, private val listRoutes: List<Route>): ArrayAdapter<Route>(mContext, 0, listRoutes){
    override fun getView(position: Int, convertView: View?, parent: ViewGroup): View {
        val layout = LayoutInflater.from(mContext).inflate(R.layout.route, parent, false)

        val route = listRoutes[position]

        layout.textView.text= route.destino
        layout.textView2.text= route.hora
        layout.textView2.text= route.dias

        return layout

    }

}