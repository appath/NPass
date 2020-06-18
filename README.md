#### NPass (Generate random password)

NPass GUI (Generate random password) - Not ready. In the process...

![NPass GUI](https://github.com/appath/NPass/blob/master/%23/%23npass_gui.png)


*****************************************

__Console version__

NPass Console Option (Generate random password)

__F.A.Q__

__how to use NPass Console?__

Unzip the downloaded archive NPass.zip, anywhere on your hard drive Example: (```C:\NPass```)

open .. ```Command line``` (CMD) now you can use it to generate random passwords,

type in console ```C:\NPass> npass.exe --help ``` for example with an argument.

__how to make sure that the console does not constantly enter the path to the executable file npass.exe?__

Quite simply, by right-clicking on the shortcut on this computer, from the pop-up menu, select 

Properties-> Advanced system settings-> Advanced-> Environment variables in the User Environment Variables window for <USER>

select item Path click on the <Modify> button, click on the <Create> button again and in the line enter the path ```C:\NPass\bin```
  
don't forget to confirm everything.

That's all now, no need to constantly enter paths just in the (CMD) console Example: ```C:\Users\appath> npass -l 27 -c 7```
