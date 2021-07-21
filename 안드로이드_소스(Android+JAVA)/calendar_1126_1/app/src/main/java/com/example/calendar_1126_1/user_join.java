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

public class user_join {

    public String link = "http://doran2322.iptime.org:8080/db.php?FLAG=";
    public String tablename;
    public List<String> data;
    public String filter;
    public String result;

    final static MainActivity mainActivity = new MainActivity();

    ArrayList<Users> tmp_usersArrayList = mainActivity.user_list;


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



    public boolean check_id_overlap(String input_id){

        boolean return_value = true;

        for(int i = 0; i<tmp_usersArrayList.size(); i++)
        {
            if (tmp_usersArrayList.get(i).getID().equals(input_id))
            {
                return_value = false;
            }
        }

        return return_value;
    }

    public void join_user(String id, String password, String name, String tel){

        List<String> join_data = new ArrayList<>();

        ArrayList<Users> to_add_user_list = mainActivity.user_list;

        Users to_add_users = new Users();

        to_add_users.setID(id);
        to_add_users.setPW(password);
        to_add_users.setNAME(name);
        to_add_users.setTEL(tel);
        to_add_user_list.add(to_add_users);

        join_data.add(id);
        join_data.add(password);
        join_data.add(name);
        join_data.add(tel);

        insert("MIRRORUSER", join_data);
    }
}
