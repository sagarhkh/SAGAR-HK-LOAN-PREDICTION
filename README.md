The Code used in this video is below:

Sub myQuery()

Dim connection As New ADODB.connection

connection.Open "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" & ThisWorkbook.FullName & _
";Extended Properties=""Excel 12.0;HDR=YES;"";"

Dim SQLQuery As String

SQLQuery = InputBox("Enter Select Statement")

Dim rs As New ADODB.Recordset
rs.Open SQLQuery, connection

Dim rSht As Worksheet
Set rSht = ThisWorkbook.Worksheets("Results")

With rSht

.Cells.ClearContents
For i = 0 To rs.Fields.Count - 1
.Cells(1, i + 1).Value = rs.Fields(i).Name
Next i
.Range("A2").CopyFromRecordset rs

End With

connection.Close

End Sub



Copyright [yyyy] [name of copyright owner]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.