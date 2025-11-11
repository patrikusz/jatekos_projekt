using System.Collections;
using System.Collections.Generic;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

public class BackgroundMusicTest
{
    // A Test behaves as an ordinary method
    [Test]
    public void BackgroundMusicTestSimplePasses()
    {
        // Use the Assert class to test conditions
    }

    // A UnityTest behaves like a coroutine in Play Mode. In Edit Mode you can use
    // `yield return null;` to skip a frame.
    [UnityTest]
    public IEnumerator BackgroundMusicTestWithEnumeratorPasses()
    {
        var musicObject = new GameObject("MusicManager");
        var audioSource = musicObject.AddComponent<AudioSource>();
        var backgroundMusic = musicObject.AddComponent<BackgroundMusic>();

        // Dummy clip létrehozása (1 frame-nyi hang)
        var clip = AudioClip.Create("TestClip", 44100, 1, 44100, false);

        // SerializeField mezõk beállítása
        typeof(BackgroundMusic)
            .GetField("musicSource", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance)
            .SetValue(backgroundMusic, audioSource);

        typeof(BackgroundMusic)
            .GetField("musicSound", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance)
            .SetValue(backgroundMusic, clip);

        // --- Act ---
        backgroundMusic.Start();

        yield return null; // várunk 1 frame-et

        // --- Assert ---
        Assert.AreEqual(clip, audioSource.clip, "A zene clip nincs beállítva.");
        Assert.AreEqual(0.5f, audioSource.volume, "A hangerõ nincs 0.5-re állítva.");
        Assert.IsTrue(audioSource.loop, "A zene nem loop-ol.");
        Assert.IsTrue(audioSource.isPlaying, "A zene nem játszik le.");
    }
}
