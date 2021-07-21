package com.example.calendar_1126_1;

import android.util.Log;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class sche_view {
    public String link = "http://doran2322.iptime.org:8080/db.php?FLAG=";
    public String tablename;
    public List<String> data;
    public String filter;
    public String result;

    public String selectALL_DATE(String tablename, String filter, String filter_data) {
        this.tablename = tablename;
        String Json = null;

        this.link += "SELECTALL_DATE" + "&TABLENAME=" + tablename + "&ROW0=" + filter + "&ROW1=" + filter_data;

        ExecutorService executorService = Executors.newFixedThreadPool(
                Runtime.getRuntime().availableProcessors()
        );

        Callable<String> task = new Callable<String>() {
            @Override
            public String call() throws Exception {
                URL url = new URL(link);

                HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                connection.setRequestMethod("GET"); //전송방식
                connection.setDoOutput(true);       //데이터를 쓸 지 설정
                connection.setDoInput(true);        //데이터를 읽어올지 설정
                String result;
                InputStream is = connection.getInputStream();
                StringBuilder sb = new StringBuilder();
                BufferedReader br = new BufferedReader(new InputStreamReader(is, "UTF-8"));
                while ((result = br.readLine()) != null) {
                    sb.append(result + "\n");
                }

                result = sb.toString();

                return result;
            }
        };
        Future<String> future = executorService.submit(task);

        try {
            Json = future.get();//작업이 잘 완료되면 예외 안남. 작업이 실패하면 예외 뱉음.
        } catch (Exception e) {
            Log.v("error", e.getMessage());
        }
        executorService.shutdown();

        return Json;
    }

    public void event_selectAll(ArrayList<Events> eventsArrayList,String id_value){
        try {
            String json = selectALL_DATE("DETAILDAY","ID",id_value);
            JSONObject j = new JSONObject(json);
            JSONArray jArray = j.getJSONArray("selectAll");
            Log.v("aaasddds",jArray.toString());

            for (int i = 0; i < jArray.length(); i++) {
                JSONObject obj = jArray.getJSONObject(i);
                if(obj.getString("ROW0").equals(id_value)) {
                    Log.v("id_value_okok",obj.getString("ROW0"));
                    Events temp_events = new Events();
                    temp_events.setID(obj.getString("ROW0"));
                    temp_events.setDate(obj.getString("ROW1"));
                    temp_events.setEvent(obj.getString("ROW2"));
                    temp_events.setItem(obj.getString("ROW3"));
                    eventsArrayList.add(temp_events);
                }
            }
        }
        catch (JSONException e){
            e.printStackTrace();
        }
    }
    public ArrayList event_day_selectAll(ArrayList<Events> eventsArrayList,String date){
        try {
            String json = selectALL_DATE("DETAILDAY","TIME",date);
            JSONObject j = new JSONObject(json);
            JSONArray jArray = j.getJSONArray("selectAll_DATE");

            for (int i = 0; i < jArray.length(); i++) {
                JSONObject obj = jArray.getJSONObject(i);
                Events temp_events = new Events();
                temp_events.setID(obj.getString("ROW0"));
                temp_events.setDate(obj.getString("ROW1"));
                temp_events.setEvent(obj.getString("ROW2"));
                temp_events.setItem(obj.getString("ROW3"));
                eventsArrayList.add(temp_events);
            }
        }
        catch (JSONException e){
            e.printStackTrace();
        }
        return eventsArrayList;
    }

    public ArrayList<Events> view_choiced_oneday(String php_date_format,String logined_ID)
    {
        ArrayList<Events> tmp_eventsArrayList = new ArrayList<>();
        ArrayList<Events> result_eventsArrayList = new ArrayList<>();
        event_day_selectAll(tmp_eventsArrayList,php_date_format);
        for(int i = 0; i<tmp_eventsArrayList.size(); i++)
        {
            if(logined_ID.equals(tmp_eventsArrayList.get(i).getID()))
            {
                Events temp_events = new Events();
                temp_events.setDate(tmp_eventsArrayList.get(i).getDate());
                temp_events.setEvent(tmp_eventsArrayList.get(i).getEvent());
                temp_events.setItem(tmp_eventsArrayList.get(i).getItem());
                result_eventsArrayList.add(temp_events);
            }
        }
        return result_eventsArrayList;
    }


    public void event_view(ArrayList<Events> eventsArrayList,String id)
    {
        event_selectAll(eventsArrayList,id);
    }

}
