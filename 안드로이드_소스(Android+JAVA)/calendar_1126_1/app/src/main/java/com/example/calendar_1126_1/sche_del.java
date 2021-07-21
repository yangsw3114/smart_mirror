package com.example.calendar_1126_1;

import android.util.Log;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.List;

public class sche_del {
    public String link = "http://doran2322.iptime.org:8080/db.php?FLAG=";
    public String tablename;
    public List<String> data;
    public String filter;
    public String result;

    public void delete(String tablename, String filter1, String data1, String filter2, String data2) {
        this.tablename = tablename;

        this.link += "DELETE" + "&TABLENAME=" + tablename + "&ROW0=" + filter1 + "&ROW1=" + data1 + "&ROW2=" + filter2 + "&ROW3=" + data2;
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

                } catch (MalformedURLException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }.start();
    }


    public void delete_event(String id, String time)
    {
        delete("DETAILDAY","ID",id,"TIME",time);
    }
}
