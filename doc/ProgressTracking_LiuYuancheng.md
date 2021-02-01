# Progress Tracking
[TOC]

##### 16/03/2020 - 20/03/2020

------

1. Added the deployed gateway information panel.(click the gateway name will link to each gateway's Individual page )
2. Added all gateway history of exception log information display panel.



##### 23/03/2020 - 30/03/2020

------

1. Did four summer intern student online interview with ShiJing.



##### 01/04/2020 - 10/04/2020

------

1. Added 3 knowledge sharing topic.
2.  Improve the UPD module communication protocol for re-connection and time out handling. 



##### 13/04/2020 - 21/04/2020

------

1. Add one knowledge sharing topic about UDP timeout error handling.
2.  Fixed the UDP communication part disconnection error.
3. Continuous to do DPDK set up.



##### 23/04/2020 - 26/04/2020

------

1.  Added function to handle the sending data (like a video/file) bigger than UDP buffer for the communication module[udpCom.py](This module is used to upload the gateway data to the database server).



##### 27/04/2020 - 30/04/2020

------

1.  Added the report data Queue so and split the data process part in a separate thread, So the server can response the client faster when a big number of client has connected to the server.



##### 04/05/2020 - 09/05/2020

------

1. Added a knowledge share document about the UDP channel closed problem.
2. Fixed the UDP closed bug in the [gwWebClient.py]



##### 11/05/2020 - 17/05/2020

------

1. Fixed the assignment document and the time plan for new intern Zhao Ming. 
2. Added an Android security key storage document for knowledge sharing.



##### 18/05/2020 - 22/05/2020

------

1. Finished the QSG-Topographic-Map web panel to show the communication state of different gateway devices
2. Created the main frame of the QSG map to let Zhaoming to fill the related function inside. 



##### 25/05/2020 - 29/05/2020

------

1. Made the map data update simulator program.

- The Node's activation states and the link with the link states will be generate in the DataMgr module. The inactivate link we will change its color to gray.



##### 01/06/2020 - 08/06/2020

------

1. Do code review with intern ZhaoMing.
2. Added the function to show all the node information on the makers' pop-up information box.
3. Updated the project design document, Problem and Solution document and the readme file.



##### 09/06/2020 - 14/06/2020

------

1. Update the design document of the QSG-Topographic-Map project.
2. Fixed the web-page control and filter check box  program.
3. Added the parameter handler in the QSG-Topographic-Map to so it can show the 2 gateways communication states in the individual gateway information display page.



##### 15/06/2020 - 20/06/2020

------

1. Improved the Gateway client IP/Information configure distribution manager server program. Function added: The server will feedback the Init ID confirm information, update rate, GPS registered feedback and the data base updated feed back to the client. So when a used client is moved to another place, when it is connected again, all the data in the control hub will update automatically.
2. Added the multi-request handling function in the map server to handle multiply map update request.
3. Improved the project design document to add 2 more function for intern ZhaoMing to work on.



##### 22/06/2020 - 27/06/2020

------

1. Added the gateway throughput diagram marker to indicate the time of key refresh.
2. Added the gateway information report rate adjustment drop down menu and started to re-make the gateway information display panel.
3. Added the template web and CSS file, so the map, information area, communication link display panel will use this template and follow the same design style



##### 29/06/2020 - 03/07/2020

------

1. Built the “Log.py” module which used to log all the server program running state for debug trace back.(It contents auto log Info/warning/error/detail, auto rollover when the log file more than 10Mb) We will use this module replace all the system build in print() function in python.
2. Added the database fetch model for ZhaoMing’s QSG_Topographic_Map program to link ZhaoMing’s program with our current gateway update information database.



##### 06/07/2020 - 11/07/2020

------

1. Test setup docker image on Ubuntu.
2. Try to built the qsvpn project generated by YiWen.(still working)
3. Help ZhaoMing to do fix the development problem for database program integration



##### 12/07/2020 - 17/07/2020

------

1. Improved the Log module added the roll over function to auto package the log file and save in specified folder. Added the function to clear the log which is older than a specific period.
2. Create the document about docker setup and usage in the container.
3. Do code review with ZhaoMing about the QSG-Topographic-Map and fixed some small bugs.



##### 20/07/2020 - 24/07/2020

------

1. Created the BgInit.py module to provide the control function for the program which running in the system background. So we can remotely control the server program from internet to change program parameters, start/restart, pause and stop the program.
2. Finished replacing all the python built in print/warning and except with Log.Info(), Log.warning(), Log.error() and Log.except() for QSG-Topographic-Map and QSG-Manger-Hub projects.
3. Created the project KPI document draft for the web design part and the code quality improvement part for the FY20/214.
4. Working on the intern Summery for ZhaoMing as his intern ship will end thin month.



##### 27/07/2020 - 30/07/2020

------

1. Added the legend in the QSG-Topographic-Map to show the different samples meaning and plugged the map in the gateway general dashboard.
2. Did final coder review with intern ZhaoMing for his internship project and created Zhaoming’s internship feedback report.
3. Integrating QSG-Topographic-Map backend part in to QSG-Manager’s dataMgr program.



##### 03/08/2020 - 07/08/2020

------

1. Fixed ZhaoMing's QSG-Topographic-Map dataBase module and integrated the database and map panel in the Quantum safe gateway dashboard. 
2. Participated the interview for the new intern Ming En. 
3. Tested compiling the wireGuard kernel module (C version) from source on Ubutnu 20.04. 
4. Tested compiling the wireGuard Client module (Go version) from source on Windows 10.
5. Prepared the docker setup document. 



##### 10/08/2020 - 15/08/2020

------

1. Uploaded WireGuard-linux source code, WireGuard Windows client source code and created the related documents in the QS-WGVPN Repository. 

2. Did source code analyze by SourceTrail  and created the analyze report. 

3. Create the wireGuard function tracking report and intern feedback for bhuvesh gupat and  Ming En. 

4. Started to add the wireGuard in to the Dockhub's Repository.

   

Todo: how singpass save their encryption key: https://public.cloud.myinfo.gov.sg/sglogin/SingPass-login-specs-v0.1.html#section/Tutorial/Tutorial-1:-Displaying-the-SingPass-QR



------

##### 17/08/2020 - 22/08/2020

1. Did source code analyze by Source Insight for the WireGuard Linux code and created the analyze report. 
2. Setup Wireguard docker image on Ubuntu20.04
3. Uploaded the debug setting doc, WireGuard  compiling tool to github.
4. Help Yiwen to check function and program execution flow for wireGuard and test how to call the Linux user space function from the kernel module. 

------

##### 24/08/2020 - 28/08/2020

1. Added the compare document between OpenCPN and WireGuard. 
2. Followed the Ubuntu/debain software installer package document to create the installer for WireGuard. Link: https://packaging.ubuntu.com/html/packaging-new-software.html
3. Followed the IBM usermode-helper API document to test call the user-space program from the kernel space.Link https://developer.ibm.com/technologies/linux/articles/l-user-space-apps/
4. 

------

##### 31/08/2020 - 04/09/2020

1. Create the docker container ID record program to check the container ID if we run the docker in background.(if multiple container is running.) : https://www.runoob.com/docker/docker-tutorial.html
2. Created the first installation .deb package which can pass the dpkg lintian check. 
3. Testing Submitting for inclusion as a Personal Package Archive so we can use apt-get install to install in on ubuntu. (Currently got another problem when I tried another)
4. 

------

##### 07/09/2020 - 11/09/2020

1. Updated the Quantum Safe Security VPN Data Flow Architecture Diagram draft Ver 0.1.

2. Tried to follow ShiJing's document to setup KeyMangement and QS_WGVPN on Utuntu20.04. 

3. Tried the Frama-C C code Analyzer program to do the static code report for WireGurad VPN program source code. 

4. Started work on setup and build the WireGuard VPN android program.  

   

------

##### 14/09/2020 - 18/09/2020

1. Updated the Quantum Safe Security VPN Data Flow Architecture Diagram draft Ver 0.2.

2. Tested normal connection between Android wireGuard Client - Linux Server VPN connection. 

3. Continuous  do the android WireGuard VPN code analyze. 

4. Try to analyze Siew Kuen's camera-VA server wireguard ping traffic experiment diagram. 

   

------

##### 21/09/2020 - 25/09/2020

1. Finished the Trustwave employee 2020 Trustwave Required Annual Security Training curriculum cause.

2. Found the WireGuard VPN android program key setup code and tried to hardcode key to simulate the key exchange progress. 

3. Draw the VPN network config diagram for the Robot management project.

   

------

**28/09/2020 - 02/10/2020**

1. Tested the virtual IP mapping setup on Ubuntu 20.04 system. 

2. Working with ShiJing to trace the ping block problem of the Telepark WireGurad VPN VM server. 

3. Draw the VM server network setup diagram and added the problem analyze description in the   "problemAnd solution" document of the QS_WGVPN project.

4. Tried the TLS "Performance Overhead" test shown in the web which we may also use for our VPN test in the future: https://www.keycdn.com/blog/https-performance-overhead

   

------

**05/10/2020 - 09/10/2020**

1. Changed the NCS_QnA_v2.1 project network configuration diagram based on Dr. Xu Jia's comments. 

2. Tested compile a C++ function by using NDK and invoke it from the Android App. 

3. Did the shared file access test for 2 Android App will may used for the key exchange process in the future. 

4. Did the UDP information exchange between different Android App test and tried to add the UDP client in the WireGurad Android App. 

5. Updated the weekly meeting [02/10/2020]. minutes log file.  

   

------

**12/10/2020 - 16/10/2020**

1. Tested the multi-process Android app example. 

2. Checked the demo video and provide some comments. 

3. Updated the weekly meeting [09/10/2020] minutes log file. 

   

------

##### 19/10/2020 - 23/10/2020

1. Prepare the WireGuard Android App and VM server connection demo and create the detail setup document. 

2. Learn and try to compile Dr. YiWen's Key management pqkes-2.0.0-beta.

3. Learn the detail document of "2020 Data Security Index".

4. Updated the weekly meeting [23/10/2020] minutes log file. 

   

------

**28/10/2020 - 08/11/2020**

1.  Key exchange App: added the function to create a key storage file in the android external file storage to save the exchanged key. (Currently we create a individual Key exchange App to compile all Dr.YiWen's code in it to make the debug easier, it will create the key file in Android External File Storage for the Wireguard app which we changed to load key.)

2. WireGuard App: Based on Dr.YiWen's presentation dataflow section, added the extend key string load function to read the exchanged key from android external file storage.(Later we may combine the  Key exchange App into a sub thread of the WireGuard App, currently as we init the key exchange app as a NativeC++ project which is different with the WireGuard App's project type, this is why we haven't added in to the WireGuard App)

3. Created the document to explain the WireGuard linux client and android client timeout reconnection feature.(Code/parameters and the setup)

4. [Under progress] Still working on the document to list all the VPN related function which WireGuard provided. Currently added: 

   - Connection lose timeout function part. 
   - Reconnection / redo handshake establish part. 
   - Peer data transmit/receive counting function. 
   - Working: server-client peer time synchronize and latency calculation part.  

5. [Under progress] Cross compile in Key exchange App : worked with Shijin to solve the problem to import an *.so in android app and still working on import all the lib used by Dr.YiWen's program in the App. 

   **Difficult**: how to combine all the Make files into the android cmakelists.txt  as the make files are using different compiler and setting. 

   

------

##### 04/12/2020 - 11/12/2020

1. Fixed related library missing under windows during android app build using NDK. 

2. Third party lib used in PQKES2.0 cross compile: 
   -  NTL https://www.shoup.net/ntl/ [Done]
   - GMP https://gmplib.org/ [Done] 
   - GF2X v1.3.0 https://gforge.inria.fr/projects/gf2x/[working]
   - mbedTLS v2.16.4 https://tls.mbed.org/[working]
   - glog https://github.com/google/glog [not used]
   - XKCP -> libkeccak[Done]

3. Fixed the CmakeList.txt file to import the additional library.  

   

------

##### 13/12/2020 - 19/12/2020

1. Re-build the test environment(install all the lib, NDK, cmake, IDE and android studio) on the new VM Ubuntu 20.04. 

2. Try to set Dr.YiWen's latest QS_WGVPN on the VM. (Met a problem: during the last make process for the IPC_service_server_client.cpp got a error of function BIO_dump_fp(), based on Dr.YIWen 's comments use openssl3.0.0 should solve the problem.) Currently I changed to openSSL 3.0.0 alpha 9 but the problem still happens, still working on fix it. 

3. Rebuild WireGuard App, key exchange App on the new test environment .(Current problem is and phone can not detect by the Linux android studio on the VM)

   

------

##### 21/12/2020 - 25/12/2020

1. Added the server IP filling text area of in the Key exchange app. 

2. Fixed part of the function invoke problem for the key exchange C code compile. Currently working on fixing the header file linkage error. (https://stackoverflow.com/questions/22159183/android-ndk-jni-undefined-reference-to-function-defined-in-custom-header-fil)

3. Added a key load selection button to control load key file from the wireGuard App.

   

------

Andriod App Feature: 

WireGuard-β Android App:

1. VPN function connect to the wireGuard Linux server. (original)

2. Access phone shared storage to load the key from the key file(After Check whether the key file has expired).

3. Auto VPN hand-shake establish and reconnect after key exchanged.(Under development) 

4. VPN Persistent Keepalive function.  



Key Exchange App: 

1. Load the IP table and gateway config file, then search all the related used key exchange file from the share folder. 

2. Key server connection test function. 

3. Save the generate key in phone shared storage. 

4. Package YiWen's key Exchange program in JNI function: GMP, openssl, mbed pass, gf2x under editing. 



------

##### 04/01/2021 - 07/01/2021

1. Worked with YIWen to fixed the compiled error of key Exchange management error course by bio.h's Bio_dump_file function error during the compilation on my side. 

2. Added the Log(tag) pop-up display in the WireGuard-β and key exchange app so during installed the 2 app  on other phone with apk file user can track the error directly during the App running. Fixed the GW configure file glob/config() function called  and file fetch+load part which related Key exchange init function. Fixed the App permission setting part and added the App permission request. (Now only set file access permission once in the phone's APP setting part) 

3. Create the user development and usage menu for WireGuard-β and Key exchange app. 

   

------

**25/01/2021 - 29/01/2021**

1. I changed the KeyEchange App to a function module and added with the header file. But the way to package the keyExchange to a dynamic *.so and use it in the phone got a problem which is the linker problem: as the linker link the function to some linux system lib. So during running the app can not load the function from the Jni wrapper correctly.  

2. I am working with YIWen to removed some of the not used function from the CtcpComm part, but for the 14 modules the code shows all of them are used.  

3. I temporary removed shared part function and only compile the init part of the keyServer, this can compile normally, the shared function added then got 5 errors.
