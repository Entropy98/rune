// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class rune : ModuleRules
{
	public rune(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;

		PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "HeadMountedDisplay" });
	}
}
