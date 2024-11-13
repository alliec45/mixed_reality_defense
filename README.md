# Mixed Reality Defense 

This repository hosts the BURGS Project "AR Security", also known as Mixed Reality Defense. This repository hosts all of the team's work to investigate how performance indicators can be exploited to expose a MR User's location type. The project began with the an AR headset called the Magic Leap 2. 

Author(s): 
Allie Craddock (alliec45@vt.edu) | 
Casie Peng (casiepeng@vt.edu) | 

# Repository Structure 
 
 - [`/scans`](https://github.com/alliec45/mixed_reality_defense/tree/main/scans): Contains all necessary information from scanning with the headset. 
    - [`/power_profiler_scan`](https://github.com/alliec45/mixed_reality_defense/tree/main/scans/power_profiler_scan): contains CSVs of performance indicator data collected from the Power Profiler
    - [`/data_analysis`](https://github.com/alliec45/mixed_reality_defense/tree/main/scans/data_analysis): outputs in the form of statistic tables and time-series graphs
    - [`scan_analysis.ipynb`](https://github.com/alliec45/mixed_reality_defense/blob/main/scans/scan_analysis.ipynb): contains the code which uses `eda.py` and `plot.py` to analyze the CSVs from `/power_profiler_scan`
    - [`eda.py`](https://github.com/alliec45/mixed_reality_defense/blob/main/scans/eda.py): functions which use the `pandas` library for Exploratory Data Analysis (EDA)
    - [`plot.py`](https://github.com/alliec45/mixed_reality_defense/blob/main/scans/plot.py). functions which use the `matplotlib` library for graphical analysis  
- [`/video_captures`](https://github.com/alliec45/mixed_reality_defense/tree/main/video_captures): Contains all videography and photography from the headset. 
- [`/weekly_updates`](https://github.com/alliec45/mixed_reality_defense/tree/main/weekly_updates): Contains weekly updates from the team since the beginning of the project. 

# Literature Review 
## Research Papers:
- [It's All in Your Headset](https://www.usenix.org/system/files/sec23fall-prepub-131-zhang-yicheng.pdf)
    - Purpose - Find side-channel attacks through hand movements, concurrent applications, and location detection. 
    - Programs - Python, C#, Memory allocation API (AppMemoryUsage), CPU, GPU, Vertex Count, Game thread time, Render thread time, backgroundTaskHost
    - Technology - Hololens, MetaQuest2
- [Apple Vision Pro’s Eye Tracking Exposed What People Type](https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.wired.com%2Fstory%2Fapple-vision-pro-persona-eye-tracking-spy-typing%2F&data=05%7C02%7Ccasiepeng%40vt.edu%7C3f171c6378b241fd2df408dcd382f7ba%7C6095688410ad40fa863d4f32c1e3a37a%7C0%7C0%7C638617806691080948%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=XhRvlu5DaztAClu0slOXyrVsUOf8wvRaxJPwVpEvSAI%3D&reserved=0)
    - Purpose - informed of the accuracy of attacks on user's keyboard inputs from eye tracking in Apple Vision Pro
    - Technology - Apple Vision Pro 
- [Inferring Semantic Location from Spatial Maps in Mixed Reality](https://habiba-farrukh.github.io/files/LocIn.pdf)
    - Purpose - Create a framework which is able to predict locations for location-detection attacks (LocIn)
    - Programs - Microsoft MRTK's Spatial Mapping 
    - Technology - HoloLens 2
- [OVR seen: Auditing Network Traffic and Privacy Policies in Oculus VR](https://www.usenix.org/system/files/sec22-trimananda.pdf)
    - Purpose - To demonstrate how cyber attackers can get access to application information from a VR headset through network traffic. 
    - Programs - OVRSeen, PolicyLint, PoliCheck, and Polisis. AntMonitor, Frida client, standard Android library, the Mbed TLS library provided by the Unity SDK, and the Unreal version of the OpenSSL library. Here's a github of their programs (which gave them access to applications): https://github.com/UCI-Networking-Group/OVRseen 
    - Technology - Oculus, Quest 2

## Tutorials: 
- [Magic Leap 2 Tools & Unity - Tutorial (Video)](https://www.youtube.com/watch?v=KqH0zv3e2AY)
    - Purpose - Setup ML2, tools to interact with ML2 and setting up the Hub with Unity Hub. 
    - Programs - Unity
    - Technology - ML2  
- [Device Stream from Magic Leap Hub 3](https://www.magicleap.care/hc/en-us/articles/6589955346957-Device-Stream)
    - Purpose: how to connect the AR headset to your device to stream and share files. 
- [How to Save Meshing Samples With ML2](https://forum.magicleap.cloud/t/how-to-save-meshes-from-ml2-meshing-sample-or-the-spaces-app/4040/4?u=alliec45)
    - Purpose: how to save mesh files from ML2 to to the computer for later studying. Compare mesh sample size with performance indicators. 
- [Magic Leap Development: Adding Spatial Mapper, Placement Feature, and Controller](https://www.youtube.com/watch?v=Ols3g_BHv1I)
    - Purpose: how to set up a Unity program that will take a mesh scan of the surroundings. 
- [Magic Leap Development: Simple Meshing](https://developer-docs.magicleap.cloud/docs/guides/unity/perception/meshing/unity-simple-meshing/)
    - Purpose: set up a simple meshing in Unity

## API/Library Documentation:
- [Magic Leap 2 Hub 3](https://developer-docs.magicleap.cloud/docs/guides/developer-tools/ml-hub-3/get-started/)
- [Magic Leap 2 Unity OpenXR](https://developer-docs.magicleap.cloud/docs/category/unity-openxr/)
- [Unity FrameTimeManager API](https://unity.com/blog/engine-platform/detecting-performance-bottlenecks-with-unity-frame-timing-manager)
- [Power Profiler Package](https://developer-docs.magicleap.cloud/docs/device/power/power-profiler/#)
- [Radeon GPU Profiler Package](https://developer-docs.magicleap.cloud/docs/guides/developer-tools/lumin-aosp-tools/radeon-gpu-profiler/)
- [Pandas Library](https://pandas.pydata.org/docs/)
- [Matplotlib Library](https://matplotlib.org/stable/index.html)

# Future Goals: 
1. More Complex Statistical Analysis
2. Compare Unity Scans with Headset Scans
3. Develop Unity Program Code (add exit features, saving features, etc.)
4. Compare Mesh Scans with Performance Indicators
5. Add More Room Types
6. Compare Headset PIs before and after scanning
7. Bring Headset Outside 
