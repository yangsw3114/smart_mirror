package com.example.calendar_1126_1;

import android.util.Log;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class dbGet {

    public String link = "http://doran2322.iptime.org:8080/db.php?FLAG=";
    public String tablename;
    public List<String> data;
    public String filter;
    public String result;

    public void update(String tablename, String filter1, String filter_data1,String filter2,String filter_data2,String u_filter1,String u_data1,String u_filter2,String u_data2,String u_filter3,String u_data3) {
        this.tablename = tablename;

        this.link += "UPDATE" + "&TABLENAME=" + tablename + "&ROW0=" + filter1 + "&ROW1=" + filter_data1 + "&ROW2=" + filter2 + "&ROW3=" + filter_data2 + "&ROW4=" + u_filter1 + "&ROW5=" + u_data1 + "&ROW6=" + u_filter2 + "&ROW7=" + u_data2 + "&ROW8=" + u_filter3 + "&ROW9=" + u_data3;
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

    public String selectALL(String tablename) {
        this.tablename = tablename;
        String Json = null;

        this.link += "SELECTALL" + "&TABLENAME=" + tablename;

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

    public String select(String tablename, String filter, String data) {
        this.tablename = tablename;
        this.filter = filter;
        String Json = null;

        this.link += "SELECT" + "&TABLENAME=" + tablename + "&ROW0=" + filter + "&ROW1=" + data;

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

    public void user_select(Users users){
        try{
            String json = select("MIRRORUSER", "ID", "a");
            JSONObject j = new JSONObject(json);
            JSONArray jArray = j.getJSONArray("select");

            for (int i = 0; i < jArray.length(); i++) {
                JSONObject obj = jArray.getJSONObject(i);
                users.setID(obj.getString("ROW0"));
            }
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    public void user_selectAll(ArrayList<Users> usersArrayList){
        try {
            String json = selectALL("MIRRORUSER");
            JSONObject j = new JSONObject(json);
            JSONArray jArray = j.getJSONArray("selectAll");

            for (int i = 0; i < jArray.length(); i++) {
                JSONObject obj = jArray.getJSONObject(i);
                Users temp_users = new Users();
                temp_users.setID(obj.getString("ROW0"));
                temp_users.setPW(obj.getString("ROW1"));
                temp_users.setNAME(obj.getString("ROW2"));
                temp_users.setTEL(obj.getString("ROW3"));
                usersArrayList.add(temp_users);
            }
        }
        catch (JSONException e){
            e.printStackTrace();
        }
    }

    public void event_selectAll(ArrayList<Events> eventsArrayList,String id_value){
        try {
            String json = selectALL_DATE("DETAILDAY","ID",id_value);
            JSONObject j = new JSONObject(json);
            JSONArray jArray = j.getJSONArray("selectAll");

            for (int i = 0; i < jArray.length(); i++) {
                JSONObject obj = jArray.getJSONObject(i);
                if(obj.getString("ROW0").equals(id_value)) {
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
}
