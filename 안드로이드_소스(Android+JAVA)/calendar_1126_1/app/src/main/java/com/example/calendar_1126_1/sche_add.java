package com.example.calendar_1126_1;

import android.util.Log;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

public class sche_add {
    public String link = "http://doran2322.iptime.org:8080/db.php?FLAG=";
    public String tablename;
    public List<String> data;
    public String result;

    public void insert(String tablename, List<String> data) {
        this.tablename = tablename;
        this.data = data;

        this.link += "INSERT" + "&TABLENAME=" + tablename;
        for (int i = 0; i < data.size(); i++) {
            this.link += "&ROW" + Integer.toString(i) + "=" + data.get(i);
        }
        Log.v("insert_check",link);

        new Thread() {
            @Override
            public void run() {
                try {
                    URL url = new URL(link);

                    HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                    connection.setRequestMethod("GET"); //전송방식
                    connection.setDoOutput(true);       //데이터를 쓸 지 설정
                    connection.setDoInput(true);        //데이터를 읽어올지 설정

                    InputStream is = connection.getInputStream();
                    StringBuilder sb = new StringBuilder();
                    BufferedReader br = new BufferedReader(new InputStreamReader(is, "UTF-8"));
                    while ((result = br.readLine()) != null) {
                        sb.append(result + "\n");
                    }

                    result = sb.toString();

                    Log.v("insert_check",result);

                } catch (MalformedURLException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }.start();
    }

    public void insert_event(String year, String month,String date,int hour, int minute,String id, String eventname, String eventitem)
    {
        String string_hour,string_minute;
        if(hour<10){ string_hour = "0"+hour; }
        else { string_hour = String.valueOf(hour); }
        if(minute<10){ string_minute = "0"+minute; }
        else { string_minute = String.valueOf(minute); }
        String str1 = month+"-"+date+"-"+year+"%20"+string_hour+":"+string_minute+":00";

        List<String> data = new ArrayList<>();

        /*data.add(id);
        data.add(str1);
        data.add(eventname);
        data.add(eventitem);*/
        data.add(eventname);
        data.add(str1);
        data.add(id);
        data.add(eventitem);


        sche_add sche_add = new sche_add();
        sche_add.insert("DETAILDAY", data);
    }

}
