
Sub Stocks()

    Dim row As Integer
    Dim year_open As Double
    Dim year_close As Double
    Dim vol_total As LongLong
    Dim last_row As Long
    
For Each ws In Worksheets
    
    row = 2
    
    ws.Range("I1:L1").Value = Array("Ticker", "Yearly Change", "Percent Change", "Total Stock Volume")
    
    last_row = ws.Cells(Rows.Count, 1).End(xlUp).row
    
    For i = 2 To last_row
    
        If ws.Cells(i - 1, 1).Value <> ws.Cells(i, 1).Value Then
            ws.Cells(row, 9).Value = ws.Cells(i, 1).Value
            year_open = ws.Cells(i, 3)
            vol_total = ws.Cells(i, 7)
            row = row + 1
        Else
            vol_total = vol_total + ws.Cells(i, 7)
            year_close = ws.Cells(i, 6)
        End If
        
        ws.Cells(row - 1, 10).Value = year_close - year_open
                
        For j = 10 To 11
        If ws.Cells(row - 1, 10) >= 0 Then
            ws.Cells(row - 1, j).Interior.ColorIndex = 4
        Else
            ws.Cells(row - 1, j).Interior.ColorIndex = 3
        End If
        Next j
            
        ws.Cells(row - 1, 11).Value = (year_close - year_open) / year_open
        ws.Cells(row - 1, 11).NumberFormat = "0.00%"
        ws.Cells(row - 1, 12).Value = vol_total
    
    Next i
    
    last_row = ws.Cells(Rows.Count, 9).End(xlUp).row
    
    Dim great_increase As Double
    Dim great_decrease As Double
    Dim great_volume As LongLong
        
    great_increase = WorksheetFunction.Max(ws.Range("K2:K" & last_row))
    great_decrease = WorksheetFunction.Min(ws.Range("K2:K" & last_row))
    great_volume = WorksheetFunction.Max(ws.Range("L2:L" & last_row))
    
    ws.Range("O2:O4").Value = Application.Transpose(Array("Greatest % Increase", "Greatest % Decrease", "Greatest Total Volume"))
    ws.Range("P1:Q1").Value = Array("Ticker", "Value")
    
    For i = 2 To last_row
    
        If ws.Cells(i, 11).Value = great_increase Then
            ws.Cells(2, 16).Value = ws.Cells(i, 9).Value
            ws.Cells(2, 17).Value = great_increase
            ws.Cells(2, 17).NumberFormat = "0.00%"
        ElseIf ws.Cells(i, 11).Value = great_decrease Then
            ws.Cells(3, 16).Value = ws.Cells(i, 9).Value
            ws.Cells(3, 17).Value = great_decrease
            ws.Cells(3, 17).NumberFormat = "0.00%"
        End If
        
        If ws.Cells(i, 12).Value = great_volume Then
            ws.Cells(4, 16).Value = ws.Cells(i, 9).Value
            ws.Cells(4, 17).Value = great_volume
            ws.Cells(2, 17).NumberFormat = "0.00%"
        End If
       
    Next i

Worksheets(ws.Name).Columns("A:Q").AutoFit

Next ws
    
End Sub
