import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    home: Scaffold(
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        backgroundColor: Colors.redAccent,
      ),
      backgroundColor: Colors.blue,
      body: const Center(
          child: Image(
        // image: AssetImage("images/shivam.jpg"),
        image: NetworkImage(
            'https://5.imimg.com/data5/AK/RA/MY-68428614/apple-500x500.jpg'),
      )),
      appBar: AppBar(
        backgroundColor: Colors.amber,
        title: const Text("My name is Shivam"),
      ),
    ),
  ));
}
