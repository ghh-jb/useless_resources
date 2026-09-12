program dynpasthon;

{$mode objfpc}{$H+}
// this is actually insane contraption, I do not write in pascal like at all and it is entirely built by ai to make it possible to use python script right inside the pascal language.
// I do not write in pascal, literally useless language rn, even arm64 assembly is more valuable
uses
	Classes, SysUtils, Process;

const
	TempScriptName = '.a20bf3369def1e2d31a1152d39ec823ca37a44376481ce271116cb2c86900bece39a94e0367f00d42f2de9dea5b2b36f068ef858ccce465f5341e403f210b25c.py';

var
	PythonProcess: TProcess;
	PythonCode: String;
	InputData: String;
	OutputString: String;
	ErrorString: String;
	Line: String;
	BytesRead: LongInt;
	Buffer: array[1..4096] of Char;
	ScriptFile: TextFile;

begin
	WriteLn('-=-= enter python code (END=eof) =-=-');
	PythonCode := '';
	while True do
	begin
		ReadLn(Line);
		if Line = 'END' then Break;
		PythonCode := PythonCode + Line + #10;
	end;

	WriteLn;
	Write('Enter the input data to send to your Python script: ');
	ReadLn(InputData);


	AssignFile(ScriptFile, TempScriptName);
	try
		Rewrite(ScriptFile);
		Write(ScriptFile, PythonCode);
	finally
		CloseFile(ScriptFile);
	end;

	PythonProcess := TProcess.Create(nil);
	try
		PythonProcess.Executable := '/usr/bin/python3';
		
		PythonProcess.Parameters.Add('-u'); 
		PythonProcess.Parameters.Add(TempScriptName);

		PythonProcess.Options := [poUsePipes, poNoConsole];
		PythonProcess.Execute;

		if Length(InputData) > 0 then
			PythonProcess.Input.Write(InputData[1], Length(InputData));
		
		Sleep(50); 
		PythonProcess.CloseInput; 

		OutputString := '';
		ErrorString := '';
		
		while PythonProcess.Running or (PythonProcess.Output.NumBytesAvailable > 0) or (PythonProcess.Stderr.NumBytesAvailable > 0) do
		begin
			if PythonProcess.Output.NumBytesAvailable > 0 then
			begin
				BytesRead := PythonProcess.Output.Read(Buffer, SizeOf(Buffer) - 1);
				if BytesRead > 0 then
				begin
					Buffer[BytesRead + 1] := #0;
					OutputString := OutputString + StrPas(@Buffer);
				end;
			end;

			if PythonProcess.Stderr.NumBytesAvailable > 0 then
			begin
				BytesRead := PythonProcess.Stderr.Read(Buffer, SizeOf(Buffer) - 1);
				if BytesRead > 0 then
				begin
					Buffer[BytesRead + 1] := #0;
					ErrorString := ErrorString + StrPas(@Buffer);
				end;
			end;

			Sleep(10);
		end;

		WriteLn;
		if Length(ErrorString) > 0 then
		begin
			WriteLn('--- Python Runtime Error Detected ---');
			Write(ErrorString);
		end else
		begin
			WriteLn('--- Pascal Received Output From Python ---');
			Write(OutputString);
		end;

	finally
		PythonProcess.Free;
		if FileExists(TempScriptName) then
			DeleteFile(TempScriptName);
	end;
end.
